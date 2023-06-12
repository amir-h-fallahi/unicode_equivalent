# Unicode equivalent
**Attacking Unicode Normalization by finding unicode equivalent characters with this tool**


#### Setup
```sh
git clone https://github.com/amir-h-fallahi/unicode_equivalent.git
cd unicode_equivalent
pip install -r requirements.txt
python3 unicode_equivalent.py
```
#### Usage
```sh
python3 unicode_equivalent.py -i ">"
python3 unicode_equivalent.py -i "<"
```
![Screenshot from 2023-06-12 16-57-46](https://github.com/amir-h-fallahi/unicode_equivalent/assets/63167700/6be73965-b4e6-4e4f-bb6b-f92f26b43ea4)

```sh
python3 unicode_equivalent.py -i "." -f NFKD
python3 unicode_equivalent.py -i "/" -f NFKD
```
![image](https://github.com/amir-h-fallahi/unicode_equivalent/assets/63167700/0a95b8ee-5103-4962-86f3-049795ced7e1)
