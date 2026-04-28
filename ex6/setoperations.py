% --- Set Operations and Parity Checks in Prolog ---

% 1. Membership: Helper predicate for set operations
is_member(X, [X|_]).
is_member(X, [_|T]) :-
    is_member(X, T).

% 2. Intersection: Elements present in both lists
intersection([], _, []).
intersection([H|T], L2, [H|Res]) :-
    is_member(H, L2),
    intersection(T, L2, Res).
intersection([H|T], L2, Res) :-
    \+ is_member(H, L2),
    intersection(T, L2, Res).

% 3. Union: Combines lists without duplicates
union([], L, L).
union([H|T], L2, Res) :-
    is_member(H, L2),
    union(T, L2, Res).
union([H|T], L2, [H|Res]) :-
    \+ is_member(H, L2),
    union(T, L2, Res).

% 4. Difference: Elements in List1 but not in List2
difference([], _, []).
difference([H|T], L2, Res) :-
    is_member(H, L2),
    difference(T, L2, Res).
difference([H|T], L2, [H|Res]) :-
    \+ is_member(H, L2),
    difference(T, L2, Res).

% 5. Subset: Checks if every element of List1 is in List2
is_subset([], _).
is_subset([H|T], L) :-
    is_member(H, L),
    is_subset(T, L).

% 6. Add: Adds an element to a set (only if it doesn't already exist)
add(X, Set, Set) :-
    is_member(X, Set).
add(X, Set, [X|Set]) :-
    \+ is_member(X, Set).

% 7. Is_Even: Checks if a number is even
is_even(N) :-
    0 is N mod 2.

% 8. Is_Odd: Checks if a number is odd
is_odd(N) :-
    1 is N mod 2.


?-
% c:/Users/Administrator/Downloads/p1.pl compiled 0.00 sec, 17 clauses
?-
|    intersection([1, 2, 3, 4], [3, 4, 5, 6], Result).
Result = [3, 4] .

?- union([1, 2, 3], [3, 4, 5], Result).
Result = [1, 2, 3, 4, 5] .

?- difference([1, 2, 3, 4], [2, 4], Result).
Result = [1, 3] .

?- is_subset([1, 2], [1, 2, 3, 4]).
true .

?- add(5, [1, 2, 3], Result).
Result = [5, 1, 2, 3].

?- is_even(8).
true.

?- is_odd(9).
true.
