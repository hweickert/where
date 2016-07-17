import pytest



def test_where_first_executes():
    import where
    where.first("python")


def test_where_where_executes():
    import where
    where.where("python")


def test_where_iwhere_executes():
    import where
    where.iwhere("python")



if __name__ == "__main__":
    pytest.main([__file__, "-s"])
