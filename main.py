import bcrypt

# ----------------------------------------------------
# 1. THE "DATABASE"
# ----------------------------------------------------
# This is our fake database. It's just a Python dictionary.
# In a real app, this would be a real SQL database.
fake_db = {}

# ----------------------------------------------------
# 2. THE REGISTRATION (Hashing & Storing)
# ----------------------------------------------------
def register_user(username, password):
    """
    Takes a plain-text password, hashes it,
    and "stores" it in our fake database.
    """
    print(f"\n---REGISTERING '{username}'---")
    
    # [Image of password registration flow]
    
    # 1. PREPARATION
    # Hashing functions require bytes, not strings.
    password_bytes = password.encode('utf-8')
    
    # 2. HASHING & SALTING
    # bcrypt.gensalt() creates a new, random salt.
    # bcrypt.hashpw() combines the password and salt, then hashes.
    print("   Hashing and salting password...")
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    
    # 3. STORING
    # We decode the hash back to a string to store it (common practice).
    # We store the username and the *hash*. NEVER the plain password.
    fake_db[username] = hashed_password.decode('utf-8')
    
    print(f"   User '{username}' registered.")
    print(f"   Database now looks like this:")
    print(f"   {fake_db}")

# ----------------------------------------------------
# 3. THE VERIFICATION (Logging In)
# ----------------------------------------------------
def login_user(username, password_attempt):
    """
    Takes a password *attempt*, re-hashes it
    using the stored salt, and compares the results.
    """
    print(f"\n---ATTEMPTING LOGIN FOR '{username}'---")
    
    # [Image of password verification flow]
    
    # 1. Get the stored hash from the "database"
    if username not in fake_db:
        print("   ❌ FAILED: User not found.")
        return
        
    stored_hash_string = fake_db.get(username)
    print(f"   Found user. Their stored hash is: {stored_hash_string}")

    # 2. PREPARATION (must convert back to bytes for comparison)
    password_attempt_bytes = password_attempt.encode('utf-8')
    stored_hash_bytes = stored_hash_string.encode('utf-8')
    
    # 3. VERIFYING
    # bcrypt.checkpw() is the magic function.
    # It securely compares the plain-text attempt against the stored hash.
    # It automatically handles extracting the salt from stored_hash_bytes.
    print("   Comparing password attempt against stored hash...")
    
    if bcrypt.checkpw(password_attempt_bytes, stored_hash_bytes):
        print("   ✅ SUCCESS: Passwords match! User is logged in.")
    else:
        print("   ❌ FAILED: Passwords do not match.")

# ----------------------------------------------------
# 4. RUN THE DEMONSTRATION
# ----------------------------------------------------
# This 'if' block ensures the code only runs
# when you execute the file directly.
if __name__ == "__main__":
    
    # --- Step 1: Register a new user ---
    register_user('mishal', 'myS3cretPass!')
    
    # --- Step 2: Try to log in with the CORRECT password ---
    login_user('mishal', 'myS3cretPass!')
    
    # --- Step 3: Try to log in with the WRONG password ---
    login_user('mishal', 'wrongPassword')