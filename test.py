import json

# Load JSON data from file
with open('combined_json.json', "r") as fp:
    json_data = json.load(fp)

# ABI from the previous message
example_abi = [
    {"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_upgradedAddress", "type": "address"}], "name": "deprecate", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "deprecated", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_evilUser", "type": "address"}], "name": "addBlackList", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_from", "type": "address"}, {"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transferFrom", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "upgradedAddress", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "balances", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "maximumFee", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "_totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [], "name": "unpause", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [{"name": "_maker", "type": "address"}], "name": "getBlackListStatus", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "address"}], "name": "allowed", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "paused", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "who", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [], "name": "pause", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "getOwner", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "newBasisPoints", "type": "uint256"}, {"name": "newMaxFee", "type": "uint256"}], "name": "setParams", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "issue", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "redeem", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "remaining", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "basisPointsRate", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "isBlackListed", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_clearedUser", "type": "address"}], "name": "removeBlackList", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "MAX_UINT", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "_blackListedUser", "type": "address"}], "name": "destroyBlackFunds", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"name": "_initialSupply", "type": "uint256"}, {"name": "_name", "type": "string"}, {"name": "_symbol", "type": "string"}, {"name": "_decimals", "type": "uint256"}], "payable": False, "stateMutability": "nonpayable", "type": "constructor"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Issue", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Redeem", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "newAddress", "type": "address"}], "name": "Deprecate", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "feeBasisPoints", "type": "uint256"}, {"indexed": False, "name": "maxFee", "type": "uint256"}], "name": "Params", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "_blackListedUser", "type": "address"}, {"indexed": False, "name": "_balance", "type": "uint256"}], "name": "DestroyedBlackFunds", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}], "name": "AddedBlackList", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}], "name": "RemovedBlackList", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "name": "owner", "type": "address"}, {"indexed": True, "name": "spender", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "name": "from", "type": "address"}, {"indexed": True, "name": "to", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"},
    {"anonymous": False, "inputs": [], "name": "Pause", "type": "event"},
    {"anonymous": False, "inputs": [], "name": "Unpause", "type": "event"}
]

# Input contract address
contract_address = "0xdac17f958d2ee523a2206206994597c13d831ec7"

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

# Write the combined JSON data to a new file
with open('combined_json.json', "w") as fp:
    json.dump(json_data, fp, indent=4)
