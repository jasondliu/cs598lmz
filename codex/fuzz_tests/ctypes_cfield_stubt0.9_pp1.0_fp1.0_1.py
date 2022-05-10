import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

si_before = sys.getrefcount(S.x)
si_after = si_before + 100
for i in range(si_before, si_after):
    print(i, sys.getrefcount(S.x))
    del S.x
</code>

Para Python 3.8, retornou isto:
<code>835 841
836 842
837 843
838 844
839 845
840 846
841 847
842 848
843 849
844 850
845 851
846 852
847 853
848 854
849 855
850 856
851 857
852 858
853 859
854 860
855 861
856 862
857 863
858 864
859 865
860 866
861 867
</code>

Para  Python 3.6, retornou este:
<code>756 870
757 871
758 872
759 873
760 8
