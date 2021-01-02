# ! add to conftest.py
def pytest_json_runtest_metadata(item, call):
    if call.when == 'setup':
        data = {}
        docs = item.function.__doc__.split('\n') if item.function.__doc__ else []
        docs = [doc.strip().replace('\n', '') for doc in docs]
        data['docs'] = docs
        if data['docs']:
            data['test_title'] = docs[1] if len(docs) >= 1 else None
            data['test_description'] = "<br>".join(docs[2:len(docs) - 1])[4:]
        return data
    return {}