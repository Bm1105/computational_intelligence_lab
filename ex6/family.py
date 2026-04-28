% --- FACTS ---

% Genders
male(moolam_thirunal_rama_varma).
male(ravi_varma_koil_thampuran).
male(chithira_thirunal_balarama_varma).
male(uthradom_thirunal_marthanda_varma).
male(g_v_raja).
male(moolam_thirunal_rama_varma_vi).

female(sethu_lakshmi_bayi).
female(sethu_parvathi_bayi).
female(karthika_thirunal_lakshmi_bayi).
female(poorum_thirunal_lalithamba_bayi).

% Parent Relationships (parent(Parent, Child))
% Level 1 to 2 (Maternal Uncle/Aunt relationship is key in this system)
% Note: In this system, the "Head" of the family is often the maternal uncle.
parent(moolam_thirunal_rama_varma, sethu_lakshmi_bayi). % Great-uncle/Grand-parental figure
parent(moolam_thirunal_rama_varma, sethu_parvathi_bayi).

% Level 2 to 3
parent(sethu_parvathi_bayi, chithira_thirunal_balarama_varma).
parent(sethu_parvathi_bayi, uthradom_thirunal_marthanda_varma).
parent(sethu_parvathi_bayi, karthika_thirunal_lakshmi_bayi).
parent(ravi_varma_koil_thampuran, chithira_thirunal_balarama_varma).

parent(sethu_lakshmi_bayi, poorum_thirunal_lalithamba_bayi).

% Level 3 to 4
parent(karthika_thirunal_lakshmi_bayi, moolam_thirunal_rama_varma_vi).
parent(g_v_raja, moolam_thirunal_rama_varma_vi).

% --- RULES ---

% Basic Relationships
father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% Grandparents
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).

% Matrilineal Succession Rule (Successor is the sister's son)
successor(S, M) :- male(S), sister(M, P), parent(P, S).

% Sister and Brother
sister(S, X) :- female(S), sibling(S, X).
brother(B, X) :- male(B), sibling(B, X).


% c:/Users/Administrator/Downloads/p3.pl compiled 0.00 sec, 26 clauses
?-
|    mother(M, chithira_thirunal_balarama_varma).
M = sethu_parvathi_bayi .

?- father(F, moolam_thirunal_rama_varma_vi).
F = g_v_raja .

?- sibling(uthradom_thirunal_marthanda_varma, S).
S = chithira_thirunal_balarama_varma .

?-
|    successor(S, moolam_thirunal_rama_varma).
false.

?- sibling(P1, P2), parent(P1, chithira_thirunal_balarama_varma), parent(P2, Cousin).
P1 = sethu_parvathi_bayi,
P2 = sethu_lakshmi_bayi,
Cousin = poorum_thirunal_lalithamba_bayi .

?- male(Person); female(Person).
Person = moolam_thirunal_rama_varma .
