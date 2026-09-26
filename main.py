import importlib.util
import os


def _load_inner():
    inner = os.path.join(os.path.dirname(__file__), "foltz-wbs", "main.py")
    spec = importlib.util.spec_from_file_location("foltz_wbs_inner", inner)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    _load_inner().main()


if __name__ == "__main__":
    main()
