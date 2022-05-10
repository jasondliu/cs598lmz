import types
types.SimpleNamespace(**json.loads(json.dumps(c.to_dict())))

# For backward compatibility with kubernetes_asyncio
Client = KubeClient
ApiClient = KubeApiClient
CoreV1Api = CoreV1Api
