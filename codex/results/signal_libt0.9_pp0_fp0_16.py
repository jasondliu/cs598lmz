import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
def guide_update(*args, **kwargs):
    global guide
    guide = Guide(pguide=kwargs["pguide"])

guides = [
    guide,
    Guide(pguide=lambda x: 2*x),
    Guide(pguide=lambda x: 0.5*x),
    Guide(pguide=lambda x: 0.5*x, naive_mean=True)
]

for t in guides[1:]:
    global guide
    guide = t
    global result
    result = t.run()
    print("\n")

paths = result.to_tensors()[0]

num_samples = paths.size(0)

of = np.zeros(num_samples)
for i in range(num_samples):
    of[i] = np.exp(paths[np.array([i]),:].sum().item())

estimate = of.mean()

print("\n")
print(estimate,
