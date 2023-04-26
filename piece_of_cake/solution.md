# Piece Of Cake

Code:

```
enc_flag = ""
flag = ""
import key

#key is 1 ASCII character
assert(len(chr(key)) == 1)

for each in flag:
    each = chr(ord(each) ^ key)
    enc_flag += each

with open("flag.enc.txt", "w") as outfile:
    outfile.write(enc_flag)
    print(enc_flag)
```

The first clue we have to solving this is that it looks like every character in the flag is being XOR'd
by a key that we don't know.

```
assert(len(chr(key)) == 1)
```

This line of code tells us that the key has a length of 1 and is within the range of 0-255 due to calling char() on the key.
(We know that this key is 1 ASCII character)

## Solution

We can try brute forcing the key by trying every possible ASCII character. Here is the script for the solution:

```
with open("flag.enc.txt", "r") as infile:
    flag = infile.read()

for i in range(256):
    test = ""
    for each in flag:
        each = chr(ord(each) ^ i)
        test += each
    try:
        print(test + '\n')
    except:
        continue
```

After running this script, we get the output:

```
dXCoS[oXo|IB

eYzF]qMEqFqbW\

{G\pLDpGpcV]

Dx!cOs${#Ox$%O\$i#b%

Ey bNr%z"Ny%$N]%h"c$

Fz#aMq&y!Mz&'M^&k!`'

G{"`Lp'x L{'&L_'j a&

@|%gKw 'K| !KX m'f!

A}$fJv!~&J}! JY!l&g 

B~'eIu"}%I~"#IZ"o%d#

C&dHt#|$H#"H[#n$e"

Lp)kG{,s+Gp,-GT,a+j-

Mq(jFz-r*Fq-,FU-`*k,

Nr+iEy.q)Er./EV.c)h/

Os*hDx/p(Ds/.DW/b(i.

Ht-oC(w/Ct()CP(e/n)

Iu,nB~)v.Bu)(BQ)d.o(

Jv/mA}*u-Av*+AR*g-l+

Kw.l@|+t,@w+*@S+f,m*

Th1s_c4k3_h45_L4y3r5

Ui0r^b5j2^i54^M5x2s4

Vj3q]a6i1]j67]N6{1p7

Wk2p\`7h0\k76\O7z0q6

Pl5w[g0o7[l01[H0}7v1

Qm4vZf1n6Zm10ZI1|6w0

Rn7uYe2m5Yn23YJ25t3

So6tXd3l4Xo32XK3~4u2

\`9{Wk<c;W`<=WD<q;z=

]a8zVj=b:Va=<VE=p:{<

^b;yUi>a9Ub>?UF>s9x?

_c:xTh?`8Tc?>TG?r8y>

Xd=So8g?Sd89S@8u?~9

Ye<~Rn9f>Re98RA9t>8

Zf?}Qm:e=Qf:;QB:w=|;

[g>|Pl;d<Pg;:PC;v<}:

$A/DC/DE/<D	CE

%@.EB.ED.=EBD

&C-FA-FG->FA:_1
Z]1Z[1"Z][

;^0[\0[Z0#[\Z

8a#3d;c8ded)c"e

9`"2e:b9ede(b#d

:c!
1f9a
:fg
f+a g

;b 0g8`;gfg*`!f

/v4$s,t/srs>t5r

 y;+|#{ |}|1{:}

!x:*}"z!}|}0z;|

"{9)~!y"~~3y8

#z8( x#~2x9~

$}?/x'$xy�������������ܤ��

�������������ݥ��

�������������ަ��

�������������ߧ��

��������������ؠ���

��������������١��

��������������ڢ��

��������������ۣ��

����������Ԭ��

����������խ��

����������֮��

����������ׯ��

��������������Ш��

��������������ѩ��

��������������Ҫ��

��������������ӫ���

�������贵�̴���

�������鵴�͵���

�������궷�ζ���

�������뷶�Ϸ���

�������찱�Ȱ����

������������ɱ����

���������ʲ����

�������ﳲ�˳����

�������༽�ļ���

�������ὼ�Ž���

�������⾿�ƾ���

�������㿾�ǿ���

�������丹�������

�������幸�������

��������溻�º����

�������绺�û����
```

The flag is the only text in this that is readable.

Flag:

> {WSUCDC:Th1s_c4k3_h45_L4y3r5}