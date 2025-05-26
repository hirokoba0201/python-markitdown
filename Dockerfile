# markitdownを使用するPython実行環境（インタラクティブ対応）
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコピー（依存関係がある場合）
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# 追加でmarkitdownの全機能を確認してインストール
RUN pip install --no-cache-dir "markitdown[all]"

# アプリケーションコードをコピー
COPY . .

# インタラクティブモードでPythonスクリプトを実行
CMD ["python", "-u", "converter.py"]