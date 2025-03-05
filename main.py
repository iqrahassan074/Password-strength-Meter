import streamlit as st
import re
import math
import string
from collections import Counter


def calculate_entropy(password):
    
    freqs = Counter(password)
    entropy = 0
    password_len = len(password)
    
   
    for count in freqs.values():
        prob = count / password_len
        entropy -= prob * math.log(prob, 2)
    
    return entropy


def is_weak_password(password):
    common_passwords = ['password', '12345', 'qwerty', '123456789', 'letmein']
    dictionary_words = ['apple', 'dog', 'cat', 'sunshine', 'password']
    
   
    if len(password) < 8:
        return True
    
   
    if password.lower() in common_passwords or any(word in password.lower() for word in dictionary_words):
        return True
    
    
    entropy = calculate_entropy(password)
    if entropy < 3.0:
        return True
    
    return False

def is_strong_password(password):
 
    if len(password) < 12:
        return False
    
    
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@#$%^&+=!.,?]', password):
        return False
    
   
    entropy = calculate_entropy(password)
    if entropy < 4.0:
        return False
    
    return True


def check_password_strength(password):
    score = 0
    feedback = []

    
    if is_weak_password(password):
        return "Weak", ["Your password is weak. Consider using a longer, more complex password with a mix of characters."]
    
  
    if is_strong_password(password):
        return "Strong", ["Your password is strong. Well done!"]
    
   
    return "Moderate", ["Your password is okay, but could be stronger. Consider adding more characters and variety."]


st.title("Password Strength Meter")


password = st.text_input("Enter your password", type='password')


if password:
    strength, feedback = check_password_strength(password)

   
    if strength == "Weak":
        st.error("Your password is weak.")
    elif strength == "Strong":
        st.success("Your password is strong.")
    else:
        st.warning("Your password is moderate.")

    for msg in feedback:
        st.write(msg)

  
    if strength == "Weak":
        st.progress(20)  
    elif strength == "Strong":
        st.progress(100)
    else:
        st.progress(60)

    st.write("\n### Suggestions:")
    if strength == "Weak":
        st.write("- Increase password length (at least 12 characters).")
        st.write("- Avoid using common passwords or dictionary words.")
        st.write("- Add a mix of uppercase, lowercase, numbers, and special characters.")
    elif strength == "Moderate":
        st.write("- Make your password longer and more varied.")
        st.write("- Include more character types for better strength.")
else:
    st.info("Please enter a password to check its strength.")
