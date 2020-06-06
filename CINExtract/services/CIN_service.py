

class CIN():
    def __init__(self, string):
        self.listing_status = string[0]
        self.industry_code = string[1:6]
        self.state_code = string[6:8]
        self.incorporation_year = string[8:12]
        self.ownership_code = string[12: 15]
        self.registration_number = string[15:]

    def get_listing_status_details(self):
        if self.listing_status == 'U':
            return "Not Listed"
        elif self.listing_status == 'L':
            return "Listed"

    def get_state_details(self):
        state_dict = {
            'AP': 'Andhra Pradesh', 'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BR',
            'CG': 'Chhattisgarh', 'Goa': 'GA', 'GJ': 'Gujarat',
            'HR': 'Haryana', 'HP': 'Himachal Pradesh', 'JH': "Jharkhand", 'KA': 'Karnataka',
            'KL': 'Kerala', 'MP': 'Madhya Pradesh', 'MH': "Maharastra", 'MN': 'Manipur',
            'ML': 'Meghalaya', 'MZ': 'Mizoram', 'NL': 'Nagaland', 'OD': 'Odisha',
            'PB': "Punjab", 'RJ': 'Rajasthan', 'SK': 'Sikkim', 'TN': 'Tamilnadu',
            'TG': "Telangana", 'TR': 'Tripura', 'UP': "Uttar Pradesh", 'UK': 'Uttarakhand', 
            'WB': "West Bengal", 'AN': "Andaman and Nicobar Islands", 'DL': "Delhi",
            'CH': 'Chandigarh', 'JK': 'Jammu and Kashmir', 'LA': 'Ladakh',
            'LD': 'Lakshadweep', 'PY': 'Puducherry'
        }
        return state_dict[self.state_code]

    def get_company_type(self):
        company_dict = {
            'PLC': 'Public Limited Compnay', 'PTC': 'Private Limited Company'
        }
        return company_dict[self.ownership_code]


    def get_details(self):
        return {
            'listing_status': self.get_listing_status_details(),
            'industry_code': self.industry_code,
            'state_code': self.get_state_details(),
            'incorporation_year': self.incorporation_year,
            'ownership': self.get_company_type(),
            'registration_number': self.registration_number
        }

if __name__ == "__main__":
    cin_obj = CIN("U74999HR2014PTC053030")
    print(cin_obj.get_details())

    