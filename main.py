from symb import SymbioticCLI

# Initialize SymbioticCLI with the correct parameters
cli_obj = SymbioticCLI(chain="mainnet", provider="https://ethereum-rpc.publicnode.com")

# Use methods directly, e.g., check if an address is a network
is_net = cli_obj.contracts["net_registry"].functions.isEntity(0x8560C667Ae72F28D09465B342A480daB28821f6b).call()
print(is_net)

