# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser

from mmdet.apis import inference_detector, init_detector,show_result_pyplot
import mmrotate  # noqa: F401


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--img',default='demo/9861.png', help='Image file')
    # parser.add_argument('--img',default='demo/demo_bridge1.jpg', help='Image file')
    parser.add_argument('--config', default='configs/oriented_rcnn/oriented_rcnn_r50_fpn_1x_dota_le90.py',help='Config file')
    parser.add_argument('--checkpoint', default='./demo/rcnn_model/oriented_rcnn_bridge_ep18.pth',help='Checkpoint file')
    parser.add_argument('--out-file', default='demo/result3.jpg', help='Path to output file')
    parser.add_argument(
        '--device', default='cuda:2', help='Device used for inference')
    parser.add_argument(
        '--palette',
        default='dota',
        choices=['dota', 'sar', 'hrsc', 'hrsc_classwise', 'random'],
        help='Color palette used for visualization')
    parser.add_argument(
        '--score-thr', type=float, default=0.3, help='bbox score threshold')
    args = parser.parse_args()
    return args


def main(args):
    # build the model from a config file and a checkpoint file
    model = init_detector(args.config, args.checkpoint, device=args.device)
    # test a single image
    result = inference_detector(model, args.img)
    # show the results
    show_result_pyplot(
        model,
        args.img,
        result,
        palette=args.palette,
        score_thr=args.score_thr,
        out_file=args.out_file)


if __name__ == '__main__':
    args = parse_args()
    main(args)

    print('done!')