import os
import glob
from markitdown import MarkItDown

# 対象ファイル test_files/ 内のファイルをリストアップ
def list_files(directory="./test_files/", extensions=None):
    """指定されたディレクトリ内のファイルをリストアップ"""
    if extensions is None:
        # markitdownがサポートする一般的な拡張子
        extensions = ['*.xlsx', '*.xls', '*.docx', '*.doc', '*.pptx', '*.ppt', 
                     '*.pdf', '*.txt', '*.md', '*.html', '*.htm', '*.csv']
    
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(directory, ext)))
        files.extend(glob.glob(os.path.join(directory, ext.upper())))
    
    return sorted(files)

def select_file():
    """ユーザーにファイルを選択させる"""
    print("=== MarkItDown ファイル変換ツール ===\n")
    
    # カレントディレクトリのファイルを取得
    files = list_files()
    
    if not files:
        print("変換可能なファイルが見つかりません。")
        print("サポートされている形式: xlsx, docx, pptx, pdf, txt, md, html, csv など")
        return None
    
    print("変換したいファイルを選択してください:\n")
    
    # ファイル一覧を表示
    for i, file in enumerate(files, 1):
        file_size = os.path.getsize(file)
        size_mb = file_size / (1024 * 1024)
        print(f"{i:2d}. {os.path.basename(file)} ({size_mb:.2f} MB)")
    
    print(f"\n0. 終了")
    
    while True:
        try:
            choice = input(f"\n番号を選択してください (0-{len(files)}): ").strip()
            
            if choice == '0':
                print("終了します。")
                return None
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(files):
                return files[choice_num - 1]
            else:
                print(f"1から{len(files)}の間の数字を入力してください。")
        
        except ValueError:
            print("有効な数字を入力してください。")
        except KeyboardInterrupt:
            print("\n終了します。")
            return None

def convert_file(file_path):
    """ファイルをMarkdownに変換"""
    try:
        print(f"\n変換中: {os.path.basename(file_path)}")
        
        markitdown = MarkItDown()
        result = markitdown.convert(file_path)
        
        # 出力ファイル名を生成
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = f"{base_name}_converted.md"
        
        # ファイルに保存
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        
        print(f"✅ 変換完了: {output_file}")
        print(f"📄 文字数: {len(result.text_content):,} 文字")
        
        # プレビューを表示
        preview = result.text_content[:500]
        print(f"\n--- プレビュー ---")
        print(preview)
        if len(result.text_content) > 500:
            print("...")
        print("--- プレビュー終了 ---\n")
        
        return output_file
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {str(e)}")
        return None

def main():
    """メイン処理"""
    while True:
        selected_file = select_file()
        
        if selected_file is None:
            break
        
        output_file = convert_file(selected_file)
        
        if output_file:
            choice = input("他のファイルも変換しますか？ (y/N): ").strip().lower()
            if choice not in ['y', 'yes']:
                break
        else:
            choice = input("他のファイルを試しますか？ (y/N): ").strip().lower()
            if choice not in ['y', 'yes']:
                break

if __name__ == "__main__":
    main()