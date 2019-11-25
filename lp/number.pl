exp(N) --> mulexp(N1), [+], exp(N2), {N is N1 + N2}
exp(N) --> mulexp(N1)

mulexp(N) --> rootexp(N1), [*], mulexp(N2), {N is N1*N2}
mulexp(N) --> rootexp(N)

rootexp(N) --> ["(exp)"]
rootexp(N) --> number(N)
