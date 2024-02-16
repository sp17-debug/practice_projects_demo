# food_donation_app.py

class FoodDonationApp:
    def __init__(self):
        self.donors = []

    def add_donor(self, name, contact, location, excess_food):
        donor_info = {
            'Name': name,
            'Contact': contact,
            'Location': location,
            'ExcessFood': excess_food
        }
        self.donors.append(donor_info)
        print(f"Thank you, {name}! Your excess food donation has been recorded.")

    def display_donors(self):
        print("\nList of Food Donors:")
        for donor in self.donors:
            print(donor)

def main():
    app = FoodDonationApp()

    while True:
        print("\nFood Donation App\n")
        print("1. Add Donor")
        print("2. Display Donors")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter your name: ")
            contact = input("Enter your contact number: ")
            location = input("Enter your location: ")
            excess_food = input("Describe your excess food: ")

            app.add_donor(name, contact, location, excess_food)

        elif choice == '2':
            app.display_donors()

        elif choice == '3':
            print("Exiting the app. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
