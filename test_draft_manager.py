"""
草案管理モジュールのテスト
"""

import unittest
import os
import shutil
from draft_manager import DraftManager


class TestDraftManager(unittest.TestCase):
    """DraftManagerクラスのテスト"""
    
    def setUp(self):
        """各テストの前に実行される初期化処理"""
        self.test_dir = "test_drafts"
        self.draft_manager = DraftManager(self.test_dir)
    
    def tearDown(self):
        """各テストの後に実行されるクリーンアップ処理"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_initialization(self):
        """初期化のテスト"""
        self.assertEqual(self.draft_manager.drafts_dir, self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))
        self.assertTrue(os.path.isdir(self.test_dir))
    
    def test_ensure_drafts_directory(self):
        """ディレクトリ作成のテスト"""
        # ディレクトリを削除
        shutil.rmtree(self.test_dir)
        self.assertFalse(os.path.exists(self.test_dir))
        
        # 再度初期化
        new_manager = DraftManager(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))
    
    def test_save_draft_without_title(self):
        """タイトルなしで草案を保存するテスト"""
        content = "# テスト草案\n\nこれはテストです。"
        filepath = self.draft_manager.save_draft(content)
        
        self.assertTrue(os.path.exists(filepath))
        self.assertTrue(filepath.startswith(self.test_dir))
        self.assertTrue(filepath.endswith('.md'))
        
        # 内容を確認
        with open(filepath, 'r', encoding='utf-8') as f:
            saved_content = f.read()
        self.assertEqual(saved_content, content)
    
    def test_save_draft_with_title(self):
        """タイトル付きで草案を保存するテスト"""
        content = "# テスト草案\n\nこれはテストです。"
        title = "テストタイトル"
        filepath = self.draft_manager.save_draft(content, title)
        
        self.assertTrue(os.path.exists(filepath))
        self.assertIn('テストタイトル', filepath)
        self.assertTrue(filepath.endswith('.md'))
    
    def test_save_draft_with_special_characters_in_title(self):
        """特殊文字を含むタイトルで草案を保存するテスト"""
        content = "# テスト草案"
        title = "テスト/タイトル?!@#$%"
        filepath = self.draft_manager.save_draft(content, title)
        
        self.assertTrue(os.path.exists(filepath))
        # ファイル名に使えない文字が除去されていることを確認
        filename = os.path.basename(filepath)
        self.assertNotIn('/', filename)
        self.assertNotIn('?', filename)
    
    def test_list_drafts_empty(self):
        """草案がない場合のリスト取得テスト"""
        drafts = self.draft_manager.list_drafts()
        self.assertEqual(len(drafts), 0)
    
    def test_list_drafts(self):
        """草案のリスト取得テスト"""
        # 複数の草案を保存
        self.draft_manager.save_draft("内容1")
        self.draft_manager.save_draft("内容2", "タイトル2")
        
        drafts = self.draft_manager.list_drafts()
        self.assertEqual(len(drafts), 2)
        
        # すべて.mdファイルであることを確認
        for draft in drafts:
            self.assertTrue(draft.endswith('.md'))
    
    def test_read_draft(self):
        """草案の読み込みテスト"""
        content = "# テスト草案\n\nこれはテストです。"
        filepath = self.draft_manager.save_draft(content)
        
        read_content = self.draft_manager.read_draft(filepath)
        self.assertEqual(read_content, content)


if __name__ == '__main__':
    unittest.main()
