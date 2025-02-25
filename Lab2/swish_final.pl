progenitor(antonita, joao).
progenitor(antonita, clara).
progenitor(antonita, francisco).
progenitor(antonita, valeria).
progenitor(antonita, ana).
progenitor(pietro, joao).
progenitor(pietro, clara).
progenitor(pietro, francisco).
progenitor(pietro, valeria).
progenitor(pietro, ana).
progenitor(ana, helena).
progenitor(ana, joana).
progenitor(joao, mario).
progenitor(helena, carlos).
progenitor(mario, carlos).
progenitor(clara, pietro).
progenitor(clara, enzo).
progenitor(jacynto, francisca).
progenitor(jacynto, antonia).
progenitor(claudia, francisca).
progenitor(claudia, antonia).
progenitor(pablo, jacynto).
progenitor(luzia, jacynto).
uniao(francisco, fabiana).
uniao(fabiana, francisco).
uniao(pietro, antonita).
uniao(antonita, pietro).
uniao(pietrosegundo, francisca).
uniao(francisca, pietrosegundo).
uniao(enzo, antonio).
uniao(antonia, enzo).
sexo(antonita, mulher).
sexo(pietro, homem).
sexo(joao, homem).
sexo(clara, mulher).
sexo(francisco, homem).
sexo(valeria, mulher).
sexo(ana, mulher).
sexo(helena, mulher).
sexo(joana, mulher).
sexo(mario, homem).
sexo(carlos, homem).
sexo(jacynto, homem).
sexo(claudia, mulher).
sexo(francisca, mulher).
sexo(antonia, mulher).
sexo(pablo, homem).
sexo(luzia, mulher).
sexo(enzo, homem).
sexo(fabiana, mulher).
sexo(pietrosegundo, homem).
sexo(antonio, homem).

irma(X,Y):-progenitor(A,X),progenitor(A,Y), X\==Y, sexo(X,mulher).
irmao(X,Y):-progenitor(A,X),progenitor(A,Y), X\==Y, sexo(X,homem).

avof(X,Y):-progenitor(X,A),progenitor(A,Y),sexo(X, mulher).
avom(X,Y):-progenitor(X,A),progenitor(A,Y),sexo(X, homem).

tio(X,Y):-progenitor(Z,Y),irmao(X,Z),sexo(X,homem).
tia(X,Y):-progenitor(Z,Y),irma(X,Z),sexo(X,mulher).

primo(X,Y):-progenitor(Z,X),tio(Z,Y),sexo(X, homem).
prima(X,Y):-progenitor(Z,X),tio(Z,Y),sexo(X, mulher).

descendente(X, Y) :- progenitor(Y, X).
descendente(X, Y) :- progenitor(Z, X), descendente(Z, Y).

ascendente(Y, X) :- progenitor(Y, X).
ascendente(Y, X) :- progenitor(Z, X), ascendente(Y, Z).





