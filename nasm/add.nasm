; Faz a soma de RAM[0] com RAM[1]

leaw $0, A%
movw (A%), D%
leaw $1, A%
addw %D, (%A), %D
leaw $2, %A
movw %D, (%A)