from ntpath import join


def update(table_name, **kwargs):
    key_param = [i for i in kwargs.keys()]
    value_param = [i for i in kwargs.values()]
    key_value = [key_param[j]+'='+f"'{value_param[j]}'" for j in range(len(key_param))]
    key_value2 = [key_param[j]+'='+"%s" for j in range(len(key_param))]
    
    test2 = ", ".join(key_value2)
    print(key_value2)
    print(test2 %tuple(value_param))
    # test = f'{"=".join(key_param)}'.join(value_param)
    # print(value_param)
    # print(key_param)
    # print(key_value)
    # # print(test)
    # string_data = ", ".join(key_value)
    # print(string_data)
    items = kwargs.items()
    for i in items:
        print()
    print(type(items))
    # jo = "=".join(items[0])
name = "keang"
fname = "Thnnathat"
lname = "Chaiphutha"
Id = 1
update(table_name="test", Id=Id, name=name, fname=fname, lname=lname)

def test(**kwargs):
    query = 'UPDATE hardware_control SET Id=0, name=:name, kind = :kind, status = :status, value = :value'
    

    
# test(name="fan", kind="fan",status="on", value=1)
