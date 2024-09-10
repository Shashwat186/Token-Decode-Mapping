import json

# Example JSON data (simplified for illustration)
with open(file, "r") as fp:
    key = file.split(".")[0]
json_data = "combined_json.json"
# Example ABI (simplified for illustration)
example_abi = [
    [{"inputs":[{"internalType":"address","name":"_implementation","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"stateMutability":"payable","type":"receive"}]
]

# Input contract address
contract_address = "0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee"

def extract_functions_from_abi(abi):
    functions = {}
    for item in abi:
        if item['type'] == 'function':
            func_name = item['name']
            inputs = [input['name'] for input in item.get('inputs', [])]
            functions[func_name] = inputs
    return functions

def compare_abi_with_json(abi_functions, json_data):
    matching_contract = None
    
    for contract_id, contract_data in json_data.items():
        all_functions_match = True
        
        # Check transfer_functions
        transfer_functions = contract_data.get('transfer_functions', {})
        for func_name, func_data in transfer_functions.items():
            fields = func_data['fields']
            abi_inputs = abi_functions.get(func_name, [])
            if set(fields.values()) != set(abi_inputs):
                all_functions_match = False
                break
        
        # Check other_functions
        if all_functions_match:
            other_functions = contract_data.get('other_functions', {})
            for func_name, func_data in other_functions.items():
                fields = func_data['fields']
                abi_inputs = abi_functions.get(func_name, [])
                if set(fields.values()) != set(abi_inputs):
                    all_functions_match = False
                    break
        
        if all_functions_match:
            matching_contract = contract_id
            break
    
    return matching_contract

# Extract functions from ABI
abi_functions = extract_functions_from_abi(example_abi)

# Compare ABI functions with JSON data
contract_id = compare_abi_with_json(abi_functions, json_data)

if contract_id:
    # Replace contract ID with the given contract address
    json_data[contract_address] = json_data.pop(contract_id)
    print(f"The ABI corresponds to contract address: {contract_address}")
else:
    print("The ABI does not correspond to any known contract")

# Print updated JSON data for verification
print(json.dumps(json_data, indent=4))
