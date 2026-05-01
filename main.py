def travel_chatbot():
    print("Welcome to Codingal Travel Agency Chatbot!!")
    print("We offer 3 exciting travelling options: ")
    print("1.City")
    print("2.Mountain")
    print("3.Beaches")

    choice=input("Please type your choice: (Mountain,Beaches,City): ").strip().lower()
    if choice =="city":
        print("\nGreat Choice! Our city tours include vibrant nightlife,museums,shopping, and cultural experiences.")
        print("Top Destinations: Singapore,Dubai,Nigeria.")
    elif choice == "mountains":
        print("\nAdventure Awaits! Our mountain package include hiking,camping and breathtaking views.")
        print("Top destinations: Mount Kenya,Atlas Mountains, Mount Toubkal.")
    elif choice == "beaches":
        print("\nRelax and Unwind! Our beach package offers sunbathing,water sports and luxury resorts.")
        print("Top destinations: Seychelles,Diani Beach, Clifton Beach.")
    else:
         print("\nSorry, I didnt understand that. Please choose City, Mountain, or Beaches.")
travel_chatbot()