import hypothesis.strategies as st

def const():
    return st.integers().map(str)


def expr():
    base = const()

    def expression(children):
        return st.one_of(
            st.tuples(children, st.sampled_from(['+', '-']), children),
            st.tuples(children, st.sampled_from(['*', '/']), children),
        ).map(lambda parts: f"{parts[0]}{parts[1]}{parts[2]}")

    return st.recursive(base, expression, max_leaves=10)
