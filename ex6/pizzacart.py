
% --- PIZZA BOOKING SYSTEM ---

% 1. Database: Pizza base prices
pizza(margherita, 200).
pizza(pepperoni, 300).
pizza(veggie_feast, 250).
pizza(hawaiian, 280).

% 2. Database: Size multipliers
size_multiplier(small, 1.0).
size_multiplier(medium, 1.5).
size_multiplier(large, 2.0).

% 3. Database: Toppings and their flat costs
topping(extra_cheese, 50).
topping(mushrooms, 30).
topping(olives, 30).
topping(onions, 20).
topping(bell_peppers, 25).

% 4. Logic: Calculate total cost of a list of toppings
% Base case: empty list costs 0
topping_price([], 0).
% Recursive case: add current topping price to the rest
topping_price([H|T], Total) :-
    topping(H, Price),
    topping_price(T, Rest),
    Total is Price + Rest.

% 5. Main Booking Rule: Calculates total order price
% Usage: book_pizza(PizzaName, Size, ToppingsList, TotalPrice)
book_pizza(Name, Size, Toppings, Total) :-
    pizza(Name, BasePrice),
    size_multiplier(Size, Mult),
    topping_price(Toppings, TPrice),
    Total is (BasePrice * Mult) + TPrice.

% c:/Users/Administrator/Downloads/p2.pl compiled 0.00 sec, 0 clauses
?-
|    book_pizza(margherita, medium, [extra_cheese], Total).
Total = 350.0.

?- book_pizza(veggie_feast, large, [mushrooms, olives], Total).
Total = 560.0.

?- book_pizza(pepperoni, small, [], Total).
Total = 300.0.

?- book_pizza(hawaiian, medium, [onions], Total), Total < 500.
Total = 440.0.

?- book_pizza(Name, small, [], 300).
false.

