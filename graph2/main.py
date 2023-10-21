from DSAGraphNode import DSAGraphNode
from DSAGraph import DSAGraph
from DSAGraphNode import DSAGraphNode
from DSAHashTable import DSAHashTable
from Heaps import DSAHeap
from Heaps import DSAHeapEntry



def update_shop_info(graph):
    shop_number = input("Enter the number of the shop you want to update: ")

    # Search for the shop in the graph
    shop = graph.get_vertex(shop_number)

    if not shop:
        print("Shop not found!")
        return

    print("What would you like to update?")
    print("1. Shop Name")
    print("2. Category")
    print("3. Location")
    print("4. Rating")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        new_name = input("Enter the new shop name: ")
        shop.update_shopName(new_name)
        newwName = shop.get_shopName()
        print("Shop name changed to ", newwName)
    elif choice == 2:
        new_category = input("Enter the new category: ")
        shop.update_category(new_category)
        newwCategory = shop.get_category()
        print("Shop category changed to ", newwCategory)
    elif choice == 3:
        new_location = input("Enter the new location: ")
        shop.update_location(new_location)
        newwLocation = shop.get_location()
        print("Shop location changed to ", newwLocation)
    elif choice == 4:
        try:
            new_rating = int(input("Enter the new rating (1-5): "))
            if 1 <= new_rating <= 5:
                shop.update_rating(new_rating)
                newwRating = shop.get_rating()
                print("Shop rating changed to ", newwRating)
            else:
                print("Invalid rating!")
        except ValueError:
            print("Please enter a valid number!")
    else:
        print("Invalid choice!")






def main():
    
    shop_table = DSAHashTable(100)
    graph = DSAGraph()
    is_running = True
    filename = "/Users/harryc/Library/CloudStorage/OneDrive-Personal/Code/DSA/graph2/text_file.csv"
    DSAGraph.import_shops_from_csv(filename, graph, shop_table)
    
    while is_running:
        print("\nWelcome to the graph program!")
        print("Please choose an option")
        print("1. Add Shop")
        print("2. Delete Shop")
        print("3. Add edge")
        print("4. Delete edge")
        print("5. Display as list")
        print("6. Edit Shop")
        print("7. Breadth first search")
        print("8. Depth first search")
        print("9. Print all shops")
        print("10. Search Shops by category")
        print("11. Import shops from CSV")
        print("12. Sort Shops by rating")
        print("(x). Exit\n")
        chosen_option = input("Please choose an option: ")
        

        if chosen_option == "1":
            shop_name = input("Please enter the Shop name you want to add: ")
            shop_number = input("Please enter the Shop number : ")
            category = input("Please enter the Shop category: ")
            location = input("Please enter the Shop location: ")
            rating = int(input("Please enter the Shop rating: "))

            shop_info = graph.add_vertex(shop_name, shop_number, category, location, rating)
            shop_table.put_item(category, shop_info)
            shop_table.print_table()
           
            
            


        elif chosen_option == "2":

            vertex_to_delete = input("Please enter the Shop number you want to delete: ")

            # If the get_vertex function returns the DSAGraphNode object, extract the shop number from it
            vertex_info = graph.get_vertex(vertex_to_delete)
            if vertex_info:
                new_shop_number = vertex_info.get_shopNumber() 
            else:
                print("Vertex not found!")
                return

            shop_table.remove(new_shop_number)
            graph.delete_vertex(vertex_to_delete)

        elif chosen_option == "3":
            edge_one = input("Please enter the first Shop number you want to add the edge to: ")
            edge_two = input("Please enter the second Shop number you want to add the edge to: ")

            graph.add_edge(edge_one, edge_two)

        elif chosen_option == "4":
            edge_one = input("Please enter the first Shop number you want to delete the edge from: ")
            edge_two = input("Please enter the second Shop number you want to delete the edge from: ")

            graph.delete_edge(edge_one, edge_two)

        elif chosen_option == "5":
            graph.display_as_list()

        elif chosen_option == "6":
            update_shop_info(graph)
            

        elif chosen_option == "7":
            
            start_label = input("Enter the start shop number: ")
            end_label = input("Enter the end shop number: ")
            #print("Following is the Breadth-First Search")
            graph.breadth_first_search(start_label, end_label)


        elif chosen_option == "8":
            print("Following is the Depth-First Search")
            graph.depth_first_search()

        elif chosen_option == "9":
            shop_table.print_table()
            print("Shops printed successfully!")
        

        elif chosen_option == "10":
            category = input("Please enter the category you want to search for: ")
            try:
                shops_found = shop_table.print_table_category(category)
                if not shops_found:  # If no shops were found for the given category
                    raise ValueError
            except ValueError:
                print(f"Category '{category}' was not found.")


        elif chosen_option == "11":
            filename = input("Enter the filename to import from: ")
            DSAGraph.import_shops_from_csv(filename, graph, shop_table)
            print("Shops imported successfully!")
        
        elif chosen_option == "12":
            category = input("Please enter the category you want to search for by rating: ")
            try:
                shops_found = shop_table.print_table_category_sorted_by_rating(category)
                if not shops_found:  # If no shops were found for the given category
                    raise ValueError
            except ValueError:
                print(f"Category '{category}' was not found.")


        elif chosen_option == "x":
            is_running = False
            print("Exiting the program. Goodbye!")
            



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
