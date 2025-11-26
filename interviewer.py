"""
インタビュアーモジュール

記事作成のための質問を管理し、対話を進行するモジュール
"""


class Interviewer:
    """記事作成のためのインタビューを実施するクラス"""
    
    def __init__(self):
        """インタビュアーの初期化"""
        self.questions = [
            "記事のタイトルは何ですか？",
            "この記事のメインテーマは何ですか？",
            "想定読者はどのような人ですか？",
            "記事で伝えたい主なポイントは何ですか？（複数ある場合はカンマ区切りで入力）",
            "この記事を読んだ後、読者にどのような行動を取ってほしいですか？",
        ]
        self.answers = {}
    
    def conduct_interview(self):
        """
        インタビューを実施する
        
        Returns:
            dict: 質問と回答のペア
        """
        print("\n=== 記事作成インタビュー開始 ===\n")
        print("インタビュアーが記事について質問します。")
        print("各質問に回答してください。\n")
        
        for i, question in enumerate(self.questions, 1):
            print(f"質問 {i}/{len(self.questions)}: {question}")
            answer = input("回答: ").strip()
            
            while not answer:
                print("回答を入力してください。")
                answer = input("回答: ").strip()
            
            self.answers[question] = answer
            print()
        
        print("=== インタビュー完了 ===\n")
        return self.answers
    
    def get_summary(self):
        """
        インタビュー結果のサマリーを取得する
        
        Returns:
            str: インタビュー結果のサマリー
        """
        if not self.answers:
            return "インタビューはまだ実施されていません。"
        
        summary = "# インタビュー結果\n\n"
        for question, answer in self.answers.items():
            summary += f"**{question}**\n{answer}\n\n"
        
        return summary
