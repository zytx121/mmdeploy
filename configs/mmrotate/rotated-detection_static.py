_base_ = ['../_base_/onnx_config.py']
codebase_config = dict(
    type='mmrotate',
    task='RotatedDetection',
    post_processing=dict(
        score_threshold=0.05,
        iou_threshold=0.1,
        pre_top_k=2000,
        keep_top_k=2000))