class Clients:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def guests(self):
        return f"{self.first_name} {self.last_name}. {self.city}."


client1 = Clients("Иван", "Петров", "Москва", 50)
client2 = Clients("Michael", "Caine", "Leatherhead", 50)
client3 = Clients("Jack", "Nicholson", "Beverly Hills", 50)

client_list = [client1, client2, client3]

for guest in client_list:
    print(guest.guests())
