"""
Article Interviewer - メインアプリケーション

記事作成のためのインタビューを実施し、結果を草案として保存するツール
"""

from interviewer import Interviewer
from draft_manager import DraftManager


def create_draft_from_interview():
    """
    インタビューを実施し、結果を草案として保存する
    
    Returns:
        str: 保存した草案のファイルパス
    """
    # インタビュアーを初期化
    interviewer = Interviewer()
    
    # インタビューを実施
    answers = interviewer.conduct_interview()
    
    # インタビュー結果のサマリーを取得
    summary = interviewer.get_summary()
    
    # 草案として保存
    draft_manager = DraftManager()
    
    # タイトルを取得（最初の質問「記事のタイトルは何ですか？」の回答）
    title_question = "記事のタイトルは何ですか？"
    title = answers.get(title_question) if answers else None
    
    filepath = draft_manager.save_draft(summary, title)
    
    return filepath


def main():
    """メイン処理"""
    print("Article Interviewer へようこそ！")
    print("記事作成のためのインタビューを開始します。\n")
    
    try:
        # インタビューを実施して草案を作成
        draft_path = create_draft_from_interview()
        
        print(f"✓ インタビュー結果を草案として保存しました: {draft_path}")
        print("\n草案ファイルを確認してください。")
        
    except KeyboardInterrupt:
        print("\n\nインタビューが中断されました。")
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")


if __name__ == "__main__":
    main()
