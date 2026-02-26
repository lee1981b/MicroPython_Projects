#!/opt/bin/lv_micropython
def get_app():
    try:
        with open("run.txt") as f:
            return f.read().strip()
    except:
        return "experiments.blink"

APP = get_app()

try:
    mod = __import__(APP, None, None, ['run'])
    if hasattr(mod, "run"):
        mod.run()
    else:
        print("No run() function in", APP)
except Exception as e:
    print("App crashed:", e)
