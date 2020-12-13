# %%
import yaml


with open("mapping.yaml", "r") as f:
    mappings = yaml.load(f)

# %%
def add_invalid_mapping(mapping, invalid_mapping):
    if mapping not in invalid_mapping:
        invalid_mapping.append(mapping)
    return invalid_mapping

def test_essential_keys(mappings):
    invalid_mapping = []
    for mapping in mappings:
        if not "long_name" in mappings[mapping].keys():
            invalid_mapping = add_invalid_mapping(mapping, invalid_mapping)
        if not "contain" in mappings[mapping].keys():
            invalid_mapping = add_invalid_mapping(mapping, invalid_mapping)
    return invalid_mapping
    
def valid_keys(mappings):
    invalid_mapping = []
    for mapping in mappings:
        for key in mappings[mapping].keys():
            if key not in ("long_name", "contain", "include", "exclude"):
                invalid_mapping = add_invalid_mapping(mapping, invalid_mapping)
    return invalid_mapping

def valid_contents(mappings):
    invalid_mapping = []
    for mapping in mappings:
        if "contain" not in mappings[mapping]:
            continue
        for content in mappings[mapping]["contain"]:
            if content.endswith(".txt") and not os.path.exists(content):
                invalid_mapping = add_invalid_mapping(mapping, invalid_mapping)
            if not content.endswith(".txt") and not content in mappings:
                invalid_mapping = add_invalid_mapping(mapping, invalid_mapping)
    return invalid_mapping

# %%
not_have_essential = test_essential_keys(mappings)
invalid_keys = valid_keys(mappings)
invalid_contents = valid_contents(mappings)

if not_have_essential == invalid_keys == invalid_contents == []:
    print("全て有効なマッピングです")
else:
    print("無効なマッピングが存在します")

print("--------------------------------------------------")
print("(1) 'long_name' または 'contain' を持たないマッピング:")
print("    -", not_have_essential)
print("(2) 無効なkeyが含まれているマッピング:")
print("    -", invalid_keys)
print("(3) 'contain' に無効な要素を含むマッピング:")
print("    -", invalid_contents)
# %%
