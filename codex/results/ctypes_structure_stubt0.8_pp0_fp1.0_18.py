import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)

with open("c.dat", "w") as fout:
    s = S()
    fout.write(s.x)

with open("c.dat") as fin:
    s = S()
    fin.read(s.x)

print s.x
</code>
C code
<code>#include &lt;stdio.h&gt;

struct S {
    double x;
};

int main() {
    FILE *fp;
    fp = fopen("c.dat", "w");
    struct S *s = malloc(sizeof *s);
    s-&gt;x = 1.0;
    fwrite(s, sizeof *s, 1, fp);
    fclose(fp);

    fp = fopen("c.dat", "r");
    fread(s, sizeof *s, 1, fp);
    fclose(fp);

    printf("%lf", s-&gt;x);
}
</code>


A:


