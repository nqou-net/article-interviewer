"""
草案管理モジュール

インタビュー結果を草案として保存・管理するモジュール
"""

import os
from datetime import datetime


class DraftManager:
    """草案を管理するクラス"""
    
    def __init__(self, drafts_dir="drafts"):
        """
        草案マネージャーの初期化
        
        Args:
            drafts_dir (str): 草案を保存するディレクトリパス
        """
        self.drafts_dir = drafts_dir
        self._ensure_drafts_directory()
    
    def _ensure_drafts_directory(self):
        """草案ディレクトリが存在することを確認し、なければ作成する"""
        if not os.path.exists(self.drafts_dir):
            os.makedirs(self.drafts_dir)
            # .gitkeepファイルを作成（存在しない場合のみ）
            gitkeep_path = os.path.join(self.drafts_dir, ".gitkeep")
            if not os.path.exists(gitkeep_path):
                with open(gitkeep_path, "w") as f:
                    f.write("")
    
    def save_draft(self, content, title=None):
        """
        草案を保存する
        
        Args:
            content (str): 保存する草案の内容
            title (str, optional): 草案のタイトル（ファイル名の一部として使用）
        
        Returns:
            str: 保存したファイルのパス
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if title:
            # タイトルからファイル名に使えない文字を除去
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
            safe_title = safe_title.replace(' ', '_')
            filename = f"draft_{timestamp}_{safe_title}.md"
        else:
            filename = f"draft_{timestamp}.md"
        
        filepath = os.path.join(self.drafts_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        return filepath
    
    def list_drafts(self):
        """
        保存されている草案のリストを取得する
        
        Returns:
            list: 草案ファイルのパスのリスト
        """
        if not os.path.exists(self.drafts_dir):
            return []
        
        drafts = []
        for filename in os.listdir(self.drafts_dir):
            if filename.endswith(".md") and filename.startswith("draft_"):
                drafts.append(os.path.join(self.drafts_dir, filename))
        
        return sorted(drafts, reverse=True)
    
    def read_draft(self, filepath):
        """
        草案を読み込む
        
        Args:
            filepath (str): 読み込む草案のファイルパス
        
        Returns:
            str: 草案の内容
        
        Raises:
            FileNotFoundError: ファイルが存在しない場合
            PermissionError: ファイルの読み取り権限がない場合
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"草案ファイルが見つかりません: {filepath}")
        except PermissionError:
            raise PermissionError(f"草案ファイルの読み取り権限がありません: {filepath}")
