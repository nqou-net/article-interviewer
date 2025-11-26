"""
インタビュアーモジュールのテスト
"""

import unittest
from unittest.mock import patch
from interviewer import Interviewer


class TestInterviewer(unittest.TestCase):
    """Interviewerクラスのテスト"""
    
    def setUp(self):
        """各テストの前に実行される初期化処理"""
        self.interviewer = Interviewer()
    
    def test_initialization(self):
        """初期化のテスト"""
        self.assertIsInstance(self.interviewer.questions, list)
        self.assertGreater(len(self.interviewer.questions), 0)
        self.assertIsInstance(self.interviewer.answers, dict)
        self.assertEqual(len(self.interviewer.answers), 0)
    
    @patch('builtins.input', side_effect=[
        'テストタイトル',
        'テストテーマ',
        '初心者',
        'ポイント1, ポイント2',
        '実践する'
    ])
    @patch('builtins.print')
    def test_conduct_interview(self, mock_print, mock_input):
        """インタビュー実施のテスト"""
        answers = self.interviewer.conduct_interview()
        
        # 回答が記録されていることを確認
        self.assertEqual(len(answers), 5)
        self.assertIn('テストタイトル', answers.values())
        self.assertIn('テストテーマ', answers.values())
    
    @patch('builtins.input', side_effect=['', '有効な回答'])
    @patch('builtins.print')
    def test_empty_answer_handling(self, mock_print, mock_input):
        """空の回答の処理テスト"""
        # 1つの質問だけでテスト
        original_questions = self.interviewer.questions
        self.interviewer.questions = ['テスト質問']
        
        answers = self.interviewer.conduct_interview()
        
        # 空の回答はスキップされ、有効な回答が記録される
        self.assertEqual(answers['テスト質問'], '有効な回答')
        
        # 質問を元に戻す
        self.interviewer.questions = original_questions
    
    def test_get_summary_no_answers(self):
        """回答がない場合のサマリーテスト"""
        summary = self.interviewer.get_summary()
        self.assertIn("まだ実施されていません", summary)
    
    def test_get_summary_with_answers(self):
        """回答がある場合のサマリーテスト"""
        self.interviewer.answers = {
            '質問1': '回答1',
            '質問2': '回答2'
        }
        
        summary = self.interviewer.get_summary()
        
        self.assertIn('質問1', summary)
        self.assertIn('回答1', summary)
        self.assertIn('質問2', summary)
        self.assertIn('回答2', summary)
        self.assertIn('# インタビュー結果', summary)


if __name__ == '__main__':
    unittest.main()
