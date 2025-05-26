# 起動方法

## 準備

- docker desktop
  https://www.docker.com/ja-jp/products/docker-desktop/

## docker コマンド

```
docker compose up -d
```

```
docker exec -it markitdown-app bash
```

### コンテナ上で、以下を実行

```
python -u converter.py
```

### 備考

test_files フォルダを作成して対象ファイルを入れてください
