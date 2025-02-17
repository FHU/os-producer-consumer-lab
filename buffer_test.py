import main

#length of buffer does not change when producing
def test_empty_buffer_prod_len():
    b = main.Buffer(5)
    p = main.Producer()
    p.produce(b)
    assert len(b.items) == 5

#producers add an int to the list
def test_empty_buffer_prod_item():
    b = main.Buffer(5)
    p = main.Producer()
    p.produce(b)
    assert any(isinstance(item, int) for item in b.items) == True

#length of buffer does not change when consuming
def test_empty_buffer_cons():
    b = main.Buffer(5)
    c = main.Consumer()
    c.consume(b)
    assert len(b.items) == 5

#if empty, consumer can't consume so buffer does not change
def test_empty_buffer_cons():
    b = main.Buffer(5)
    orig_items = b.items[:]
    c = main.Consumer()
    c.consume(b)
    check_items = b.items[:]
    flag = all(x == y for x, y in zip(orig_items, check_items))
    assert flag == True

#when producing in pointer increments
def test_in_pointer():
    b = main.Buffer(5)
    p = main.Producer()
    orig_in = b.in_pointer
    p.produce(b)
    new_in = b.in_pointer
    assert new_in == orig_in + 1

#when producing out pointer does not change
def test_out_pointer():
    b = main.Buffer(5)
    p = main.Producer()
    orig_out = b.out_pointer
    p.produce(b)
    new_out = b.out_pointer
    assert new_out == orig_out

#when consuming out pointer does not change for empty buffer
def test_out_pointer_cons_empty():
    b = main.Buffer(5)
    c = main.Consumer()
    orig_out = b.out_pointer
    c.consume(b)
    new_out = b.out_pointer
    assert new_out == orig_out

#When consuming, out pointer changes
def test_out_pointer_cons():
    b = main.Buffer(2)
    c = main.Consumer()
    p = main.Producer()
    p.produce(b)
    p.produce(b)
    orig_out = b.out_pointer
    c.consume(b)
    new_out = b.out_pointer
    assert new_out == orig_out + 1

#when consuming, in pointer does not change
def test_out_pointer_cons():
    b = main.Buffer(3)
    c = main.Consumer()
    p = main.Producer()
    p.produce(b)
    p.produce(b)
    orig_in = b.in_pointer
    c.consume(b)
    new_in = b.in_pointer
    assert new_in == orig_in