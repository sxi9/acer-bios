import re, sys, collections

src = sys.argv[1]
out_md = sys.argv[2]

form_re   = re.compile(r'Form FormId: (0x[0-9A-Fa-f]+), Title: "([^"]*)"')
prompt_re = re.compile(r'(OneOf|CheckBox|Numeric) Prompt: "([^"]*)"')
opt_re    = re.compile(r'OneOfOption Option: "([^"]*)"')
help_re   = re.compile(r'Help: "([^"]*)"')

JUNK = {"", "Missing String", "InvalidId"}

# key: (form_title, prompt) -> {"type":..., "opts": ordered set, "help": str}
settings = collections.OrderedDict()
form_order = []   # unique form titles in first-seen order
cur_form = None
cur_key = None

with open(src, encoding="utf-8", errors="replace") as f:
    for line in f:
        m = form_re.search(line)
        if m:
            title = m.group(2)
            cur_form = title if title not in JUNK else None
            if cur_form and cur_form not in form_order:
                form_order.append(cur_form)
            cur_key = None
            continue
        m = prompt_re.search(line)
        if m:
            typ, prompt = m.group(1), m.group(2)
            if prompt in JUNK or cur_form is None:
                cur_key = None
                continue
            cur_key = (cur_form, prompt)
            hm = help_re.search(line)
            if cur_key not in settings:
                settings[cur_key] = {"type": typ, "opts": [], "help": hm.group(1) if hm else "", "default": None}
            continue
        m = opt_re.search(line)
        if m and cur_key:
            o = m.group(1)
            if o not in JUNK:
                if o not in settings[cur_key]["opts"]:
                    settings[cur_key]["opts"].append(o)
                if ", Default" in line and settings[cur_key]["default"] is None:
                    settings[cur_key]["default"] = o

by_form = collections.OrderedDict()
for (form, prompt), v in settings.items():
    by_form.setdefault(form, []).append((prompt, v))

with open(out_md, "w", encoding="utf-8") as w:
    w.write("# Acer Nitro AN515-43 — Full BIOS Settings Reference (from firmware IFR)\n\n")
    w.write(f"Unique settings: {len(settings)}   |   Menus/forms: {len(by_form)}\n\n")
    w.write("Legend: [select] = dropdown, [toggle] = on/off, [number] = numeric field, ★ = firmware factory default\n\n---\n\n")
    for form in form_order:
        if form not in by_form:
            continue
        items = by_form[form]
        w.write(f"## {form}  ({len(items)} settings)\n\n")
        for prompt, v in items:
            tag = {"OneOf": "select", "CheckBox": "toggle", "Numeric": "number"}[v["type"]]
            rendered = [(o + "★") if o == v["default"] else o for o in v["opts"]]
            opts = (" — " + " / ".join(rendered)) if rendered else ""
            w.write(f"- [{tag}] **{prompt}**{opts}\n")
            if v["help"] and v["help"] not in JUNK and v["help"] != prompt:
                h = v["help"].replace("\n", " ")
                if len(h) > 160: h = h[:157] + "..."
                w.write(f"    - _{h}_\n")
        w.write("\n")

print(f"unique settings: {len(settings)}")
print(f"forms: {len(by_form)}")
print("--- form list (settings count) ---")
for form in form_order:
    if form in by_form:
        print(f"{len(by_form[form]):4d}  {form}")
