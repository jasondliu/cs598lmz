import types
types.ModuleType.__repr__ = lambda m: ''  # type: ignore
types.ModuleType.__name__ = lambda m: ''  # type: ignore


def init_tracer(service: str,
                datadog_config_file: str = None,
                use_env_prefix: bool = False,
                use_env_config: bool = False) -> None:
    """
    Initialize tracer with settings from config file or env variables.

    The function uses the following procedure:
    - Considers the config file specified in ENV dd_config_file
      (eg DD_TRACE_AGENT_URL=unix:/var/run/dd-trace/dd-agent.sock)
    - If file specified, loads spans and settings from the file
    - If not specified, considers the datadog_config_file
      parameter to the init_tracer function.
    - If specified, loads settings from the specified file
    - If not specified, loads settings from the datadog.yaml
      found in the current dir.
    - If the file is not found, it is
