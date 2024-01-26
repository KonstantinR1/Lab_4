import json

# Load JSON data from the file
with open('sample-data.json') as file:
    data = json.load(file)

# Extract relevant information
interface_data = data.get('imdata', [])

# Print header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface details
for entry in interface_data:
    l1_phys_if = entry.get('l1PhysIf', {})
    attributes = l1_phys_if.get('attributes', {})
    
    dn = attributes.get('dn', '')
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))