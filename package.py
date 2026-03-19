from datetime import datetime, timedelta

# Create Package class to hold data from the package file (data/packages.csv)

class Package: 
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight_kilo, special_notes): 
        '''
        Initialize a Package object with these parameters:
        self
        package_id: the unique identifier for the package
        address: Street address for the delivery
        city: City of delivery location
        state: State of delivery location
        zip_code: Zip code of delivery location
        delivery_deadline: deadline for the package delivery (specific time deadline or by end of day/EOD)
        special_notes: Notes describing delivery constraints (such as truck requirements or grouped deliveries)
        '''
        self.package_id = int(package_id) # Store each package as an integer for easy hashing
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight_kilo = weight_kilo
        self.special_notes = special_notes
        self.time_delivered = datetime.max 
        self.truck_departure_time = datetime.min 

# Return a formatted string representation of the package 
    def __str__(self):
        return (
            #Print package ID and address information on first list
            #Print delivery deadline, package weight, and notes on second line
            f"Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code}\n"
            f"Delivery Deadline: {self.delivery_deadline}, Weight (kg): {self.weight_kilo}, Special Notes: {self.special_notes}"
            )
    '''
# Output human readable package information, not object references!
def print(self):
    print('---PACKAGE HASH TABLE---')
    for item in self.map:
        if item is not None:
            for pair in item:
                print(f"Package ID: {pair[0]}, Data: {pair[1]}")
    '''
