import json
import numpy as np
import random
from transformers import AutoModelForCausalLM, AutoTokenizer
import timeit
import torch
from torch.utils.data import SequentialSampler, DataLoader

from beam import Beam
from dataset import lineDataset

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

def eval_line_completion(model, tokenizer):
    """
    Modified version from CodeXGLUE/Code-Code/CodeCompletion-line
    """
    def DecodeIds(idxs):
        codes = ""
        for idx in idxs:
            to_add = tokenizer.convert_ids_to_tokens(idx)
            if tokenizer.convert_ids_to_tokens(idx)[0] == '\u0120':
                if not codes.endswith(" "):
                    codes += " " + to_add[1:]
                else:
                    codes += to_add[1:]
            elif (
                idx in [tokenizer.bos_token_id, tokenizer.eos_token_id, tokenizer.sep_token_id, tokenizer.pad_token_id] or
                tokenizer.convert_ids_to_tokens(idx).startswith("<NUM_LIT")
            ):
                codes += " " + to_add + " "
            else:
                codes += to_add
        return codes.strip(" ")

    model.eval()
    dataset = lineDataset(tokenizer, file_type="line")
    #dataset = lineDataset(tokenizer, args, logger, file_type=file_type, block_size=args.block_size-100)
    test_sampler = SequentialSampler(dataset)
    test_dataloader = DataLoader(dataset, sampler=test_sampler, batch_size=1)

    break_ids = [tokenizer.sep_token_id]

    for inputs in test_dataloader:
        with torch.no_grad():
            beam_size = 5
            m = torch.nn.LogSoftmax(dim=-1)
            outputs = model(inputs[:, :-1])[1]
            p = []
            zero = torch.LongTensor(1).fill_(0)
            for i in range(inputs.shape[0]):
                past = [torch.cat([x[0].unsqueeze(0),x[1].unsqueeze(0)],dim=0) if type(x)==tuple else x for x in outputs]
                past_hidden = [x[:, i:i+1].expand(-1, beam_size, -1, -1, -1) for x in past]
                beam = Beam(beam_size, inputs[i][-1].data, break_ids)
                input_ids = None
                for _ in range(100):
                    if beam.done():
                        break
                    input_ids = beam.getCurrentState()
                    outputs = model(input_ids, past_key_values=past_hidden)
                    out = m(outputs[0][:, -1, :]).data
                    beam.advance(out)
                    past = [torch.cat([x[0].unsqueeze(0),x[1].unsqueeze(0)],dim=0) if type(x)==tuple else x for x in outputs[1]]
                    past_hidden = [x.data.index_select(1, beam.getCurrentOrigin()) for x in past]
                hyp = beam.getHyp(beam.getFinal())
                pred = beam.buildTargetTokens(hyp)[:beam_size]

                pred = [torch.cat([x.view(-1) for x in p]+[zero]*(100-len(p))).view(1,-1) for p in pred]
                p.append(torch.cat(pred, 0).unsqueeze(0))
            p = torch.cat(p, 0)
            for pred in p:
                t = pred[0].numpy()
                t = t.tolist()
                if 0 in t:
                    t = t[:t.index(0)]
                text = DecodeIds(t).strip("<EOL>").strip()
                print(tokenizer.decode(inputs[0]) + text)

def line_completion(tokenizer, model):
    eval_line_completion(model, tokenizer)

def print_alert(s):
    print("[93m", s, "[0m", sep="")

def text_generation(tokenizer, model):
    #string = """def add(a, b):
    #    x = a + b"""
    #tokens = tokenizer.encode(string, return_tensors="pt")

    times = []
    for i in range(30):
        print(f"=== seed {i} {'=' * 20}")
        start = timeit.default_timer()
        set_seed(i)
        with open("data/generation.json", "r") as f:
            for line in f:
                data = json.loads(line)
                tokens = tokenizer.encode(data["input"], return_tensors="pt")

                output = model.generate(tokens,
                    max_length=250,
                    do_sample=True,
                    top_p=0.95,
                    top_k=60,
                )
                results = tokenizer.decode(output[0])
                print(results)
        end = timeit.default_timer()
        t = end - start
        times.append(t)
        print_alert(f"time elapsed: {t} s")

    print_alert(f"    mean: {np.mean(times)} s")
    print_alert(f"std. dev: {np.std(times)} s")
    print_alert(f"     min: {np.min(times)} s")
    print_alert(f"     max: {np.max(times)} s")

def load_model(adapted=False):
    ptmodel = "CodeGPT-small-py"
    if adapted:
        ptmodel += "-adaptedGPT2"
    tokenizer = AutoTokenizer.from_pretrained(ptmodel)
    model = AutoModelForCausalLM.from_pretrained(ptmodel, pad_token_id=tokenizer.eos_token_id)

    return tokenizer, model

def main():
    #tokenizer, model = load_model(adapted=True)
    #line_completion(tokenizer, model)

    tokenizer, model = load_model(adapted=True)
    text_generation(tokenizer, model)

if __name__ == "__main__":
    main()
