import pytesseract
from PIL import ImageGrab
import pyautogui
import sys

# Tesseractのパスを設定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    # スクリーンショットを取得
    print("画面のスクリーンショットを取得中...")

    screenshot = ImageGrab.grab()
    
    # OCR処理を実行
    print("OCRでテキストを認識中...")
    ocr_result = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    
    # OCR結果から "red" を検索
    target_text = "red"
    found_index = None
    
    print("\n--- 認識されたテキストと座標 ---")
    for i, text in enumerate(ocr_result['text']):
        if text.strip():  # 空文字列でない場合のみ表示
            print(f"テキスト: {text}")
            print(f"座標: x={ocr_result['left'][i]}, y={ocr_result['top'][i]}")
            print(f"サイズ: 幅={ocr_result['width'][i]}, 高さ={ocr_result['height'][i]}\n")
            
            # 大文字小文字を区別せずに "red" を検索
            if text.lower() == target_text.lower():
                found_index = i
                break
    
    if found_index is None:
        print(f'"{target_text}"が画面上で見つかりませんでした。')
        sys.exit(1)
    
    # クリック座標を計算
    click_x = ocr_result['left'][found_index] + ocr_result['width'][found_index] // 2
    click_y = ocr_result['top'][found_index] + ocr_result['height'][found_index] // 2
    
    print(f'"{target_text}" が見つかりました。クリックを実行します...')
    print(f"クリック座標: x={click_x}, y={click_y}")
    
    # クリックを実行
    pyautogui.click(click_x, click_y)
    print(f'"{target_text}" をクリックしました。')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        sys.exit(1)