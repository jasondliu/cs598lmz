import codecs
codecs.register_error("strict", codecs.ignore_errors)

def strip_audio(arquivo):
	cmd1 = commands.getoutput("sox %s -c 1 a.wav" %(arquivo));
	cmd2 = commands.getoutput("sox %s -c 1 b.wav" %(arquivo));
	cmd3 = commands.getoutput("sox %s -c 1 c.wav" %(arquivo));
	cmd4 = commands.getoutput("sox %s -c 1 d.wav" %(arquivo));
	cmd5 = commands.getoutput("sox %s -c 1 e.wav" %(arquivo));
	cmd6 = commands.getoutput("sox %s -c 1 f.wav" %(arquivo));
	return cmd1;

def deteccao_de_sinal(audio_a,tempo_limite):
	cutAudio = AudioSegment.from_wav(audio_a)
	n = 0
	i = 0
	while i < tempo_limite:
		if RMS
