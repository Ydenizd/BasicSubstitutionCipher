import string
import random


###Substitution cipher kullanmis olduk

# In this example we assumed that Aice and Bob shared the key in a securte manner.

# frekans analizine karsi zayif ama sadece brut force kullanicam 2.task benim icin cok zor gorunuyor vaktim yok 


characters = string.ascii_letters + string.digits + string.punctuation + " " + " \n"
chars = list(characters)
key = chars.copy()
random.shuffle(key)    # 95! olasılık


ciphered_text = ""
plain_text = ""


class Alice:
    
    main_text = '''From fairest creatures we desire increase, That thereby beauty's rose
                might never die, But as the riper should by time decease, His tender 
                heir might bear his memory: But thou contracted to thine own bright 
                eyes, Feed'st thy light's flame with self-substantial fuel, Making a 
                famine where abundance lies, Thy self thy foe, to thy sweet self too 
                cruel: Thou that art now the world's fresh ornament, And only herald 
                to the gaudy spring, Within thine own bud buriest thy content, And 
                tender churl mak'st waste in grading: Pity the world, or else this 
                glutton be, To eat the world's due, by the grave and thee. 
                When forty winters shall besiege thy brow, And dig deep trenches in 
                thy beauty's field, Thy youth's proud livery so gazed on now, Will be a 
                tattered weed of small worth held: Then being asked, where all thy beauty lies, 
                Where all the treasure of thy lusty days; To say within thine own deep sunken eyes, 
                Were an all-eating shame, and thriftless praise.'''

    def encryption(self, key):
        
        for i in Alice.main_text:
            index = chars.index(i)
            global ciphered_text
            ciphered_text += key[index]
        # print(ciphered_text)
        return ciphered_text


class Bob:
    
    def decryption(self, ciphered_text, key):
    

        for i in ciphered_text:
            index = key.index(i)
            global plain_text
            plain_text += chars[index]
        
        return plain_text


alice = Alice()
bob = Bob()

print(f"\n This is our key: \n {key}")

print(f"\n This is encrypted message: \n\n {alice.encryption(key)}")
print(f"\n This is decrypted message: \n\n {bob.decryption(ciphered_text, key)}")


### Brut force

#We will be trying two ways to crack the message:
   #First trying all the possibilities - first we need to check what kind of characters in use then we will create a similar key to try and find comman english words in results.
   #Second frequency analyz 
   #Oscar metnin ingilizce oldugun var sayiyor
   #Oscar sifreli metinden karakter setini tahmin edecek ve bir varsayim ile saldiri yapacak 

class Oscar:

    def __init__(self, ciphered_text):
        
        self.seen_key_members = list(set(ciphered_text))
        # print(self.seen_key_members)
        
        import string

        self.ciphered_text = ciphered_text
        self.assumed_chars = list(string.ascii_letters + string.digits + string.punctuation + " \n")

    def brute_force_attack(self, iteration):
        
        best_score = 0
        best_plaintext = ""
        best_key = None

        for i in range(iteration):
            random_key = self.assumed_chars.copy()
            random.shuffle(random_key)

            plain_text = self.try_the_key(random_key)
            score = self.calculate_fitness(plain_text)

            if score > best_score:
                best_score = score
                best_key = random_key
                best_plaintext =plain_text

                print(f"Deneme: {i} skor: {score}")
        return best_plaintext, best_key, best_score, i
    
    def try_the_key(self, key):

        plain_text = ""

        for c in self.ciphered_text:
            if c in key:
                index = key.index(c)
                plain_text += self.assumed_chars[index]

            else:
                plain_text += c
            
        return plain_text



    def calculate_fitness(self, text):

        common_words = ["the", "it", "he", "she", "and", "they", "you", "for", "to", "of"]    #4. adimda text German veya Turkce gonderilirse buradaki kelimeler calismayacak

        score = 0
        text_lower = text.lower()

        for word in common_words:
            score += text_lower.count(' ' + word + ' ')
        
        return score

# Oscar sadece şifreli metni bilir
oscar = Oscar(ciphered_text)

print("Cracking...")

cracked_text, cracked_key, score, i = oscar.brute_force_attack(iteration=2000000)

print(f"\nBest Score: {score}")
print(f"\nCracked Text:\n{cracked_text}...")


with open("task_1_results.txt", "a", encoding="utf-8") as f:
    f.write(f"Iteration: {i} \n")
    f.write(f"score: {score} \n")
    f.write(f"Cracked Key: {cracked_key} \n\n")
    f.write(f"Cracked Text: {cracked_text} \n\n\n")
