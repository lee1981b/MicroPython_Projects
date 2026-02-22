#!/opt/bin/lv_micropython
import uos as os

IS_DIR = 0x4000


def is_regular_file(file_type):
    return (file_type & IS_DIR) == 0


scripts_to_run = []
for entry in os.ilistdir():
    filename = entry[0]
    file_type = entry[1]
    if not is_regular_file(file_type):
        continue
    if not filename.endswith(".py"):
        continue
    if filename in ("boot.py", "main.py"):
        continue
    scripts_to_run.append(filename)

scripts_to_run.sort()

for filename in scripts_to_run:
    print("===============================")
    print("Running:", filename)
    print("===============================")
    try:
        with open(filename) as script:
            code = script.read()
        exec(compile(code, filename, "exec"), globals())
    except Exception as exc:
        print("Error in", filename, ":", exc)
