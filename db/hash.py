import bcrypt

class Hash():
    @staticmethod
    def bcrypt(password: str) -> str:
        # パスワードをバイトに変換
        password_bytes = password.encode('utf-8')
        # ソルトを生成
        salt = bcrypt.gensalt()
        # パスワードをハッシュ化
        hashed = bcrypt.hashpw(password_bytes, salt)
        # バイトを文字列に変換して返す
        return hashed.decode('utf-8')

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        # 文字列をバイトに変換
        hashed_bytes = hashed_password.encode('utf-8')
        plain_bytes = plain_password.encode('utf-8')
        # パスワードを検証
        return bcrypt.checkpw(plain_bytes, hashed_bytes)