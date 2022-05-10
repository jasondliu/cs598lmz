import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def cmpfunc(a,b):
    return comp(a,b)
lib.sort(array, cmpfunc)

"""

"""
template<typename T>
struct MySetComparator {
    explicit MySetComparator(const set<T>& s1, const set<T>& s2)
        : s1_compared_to_empty_(s1.empty()), s2_compared_to_empty_(s2.empty()) {
        minimum_element_of_s1_ = s1.begin();
        minimum_element_of_s2_ = s2.begin();
    }

    bool operator()(const set<T>& s1, const set<T> &s2) {
        if (s1.empty()) return !s2.empty();
        if (s2.empty()) return false;

        if (s1.first() != s2.first()) {
            return s1.first() < s2.first();
        }

        if (s1
