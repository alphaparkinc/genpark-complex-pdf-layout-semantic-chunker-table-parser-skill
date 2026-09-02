class ComplexPdfLayoutSemanticChunkerTableParserClient:
    def parse_document_layout(self, document_pdf_url='https://reports.sec.gov/filing/10k_sample.pdf', preserve_tables_as_markdown=True):
        return {
            'parser_job_id': 'pdf_prs_8812',
            'pages_processed_count': 24,
            'multi_column_text_blocks_resolved_count': 68,
            'tables_extracted_as_markdown_count': 12,
            'hierarchical_headings_ast_url': 'https://parser.genpark.ai/ast/8812.json',
            'clean_markdown_bundle_url': 'https://parser.genpark.ai/markdown/8812.md'
        }
