#include <iostream>
#include <map>
#include <string>

using namespace std;

// structure to store item details
struct Item {
  string name;
  int quantity;
  float price;
  float total;
};

int main() {
  // store customer name
  string customerName;
  cout << "Enter customer name: ";
  getline(cin, customerName);

  // store number of items
  int numItems;
  cout << "Enter number of items: ";
  cin >> numItems;

  // create a map to store item details
  map<string, Item> items;

  // input item details
  for (int i = 0; i < numItems; i++) {
    Item item;
    cout << "Enter item name: ";
    cin >> item.name;
    cout << "Enter item quantity: ";
    cin >> item.quantity;
    cout << "Enter item price: ";
    cin >> item.price;

    // calculate total price for the item
    item.total = item.quantity * item.price;

    // add item to the map
    items[item.name] = item;
  }

  // display bill
  cout << "Bill for " << customerName << ":\n";
  cout << "Item\tQuantity\tPrice\tTotal\n";
  float total = 0;
  for (auto const& [name, item] : items) {
    cout << item.name << "\t" << item.quantity << "\t\t" << item.price << "\t" << item.total << endl;
    total += item.total;
  }
  cout << "Total: " << total << endl;

  return 0;
}
