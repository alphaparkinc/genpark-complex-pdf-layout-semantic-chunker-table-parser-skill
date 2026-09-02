from client import ComplexPdfLayoutSemanticChunkerTableParserClient

def main():
    client = ComplexPdfLayoutSemanticChunkerTableParserClient()
    res = client.parse_document_layout('https://arxiv.org/pdf/2405.0001.pdf')
    print('Complex PDF Layout Parser: ' + res['parser_job_id'] + ' (' + str(res['pages_processed_count']) + ' pages)')
    print('Multi-Column Blocks: ' + str(res['multi_column_text_blocks_resolved_count']) + ' | Tables: ' + str(res['tables_extracted_as_markdown_count']))
    print('Clean Markdown: ' + res['clean_markdown_bundle_url'])

if __name__ == '__main__':
    main()
