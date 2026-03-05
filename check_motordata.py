import re, sys
try:
    import js2py
except ImportError:
    print('js2py not installed')
    sys.exit(1)
path=r"c:\Users\lenov\OneDrive\ドキュメント\Custom Office Templates\index.html"
text=open(path,'r',encoding='utf-8').read()
m=re.search(r'const motorData = \[([\s\S]*?)\];',text)
print('found', bool(m))
if not m:
    sys.exit(1)
code='['+m.group(1)+']'
try:
    arr=js2py.eval_js(code)
    print('len', len(arr))
except Exception as e:
    print('error',e)
    sys.exit(1)
