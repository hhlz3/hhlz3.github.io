<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>圣诞快乐</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden;
        }
        .tree {
            position: relative;
            width: 300px;
            height: 400px;
        }
        .star {
            position: absolute;
            top: -20px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 30px;
            background: #ffeb3b;
            clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
            animation: twinkle 1s infinite alternate;
        }
        .tree-layer {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            background: #2e7d32;
            border-radius: 50% 50% 0 0;
            animation: grow 2s ease-out forwards;
        }
        .layer1 { width: 280px; height: 100px; animation-delay: 0s; }
        .layer2 { width: 220px; height: 100px; bottom: 80px; animation-delay: 0.5s; }
        .layer3 { width: 160px; height: 100px; bottom: 160px; animation-delay: 1s; }
        .layer4 { width: 100px; height: 80px; bottom: 240px; animation-delay: 1.5s; }
        .trunk {
            position: absolute;
            bottom: -50px;
            left: 50%;
            transform: translateX(-50%);
            width: 40px;
            height: 60px;
            background: #795548;
            animation: trunkGrow 2s ease-out forwards;
            animation-delay: 2s;
        }
        .light {
            position: absolute;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            animation: blink 0.8s infinite alternate;
        }
        @keyframes twinkle {
            from { opacity: 0.7; transform: translateX(-50%) scale(0.9); }
            to { opacity: 1; transform: translateX(-50%) scale(1.1); }
        }
        @keyframes grow {
            from { height: 0; }
            to { height: 100px; }
        }
        @keyframes trunkGrow {
            from { height: 0; }
            to { height: 60px; }
        }
        @keyframes blink {
            from { opacity: 0.5; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="tree">
        <div class="star"></div>
        <div class="tree-layer layer1"></div>
        <div class="tree-layer layer2"></div>
        <div class="tree-layer layer3"></div>
        <div class="tree-layer layer4"></div>
        <div class="trunk"></div>
        <!-- 随机生成彩灯 -->
        <script>
            const tree = document.querySelector('.tree');
            const colors = ['#f44336', '#2196f3', '#ffeb3b', '#9c27b0', '#4caf50'];
            for(let i = 0; i < 30; i++) {
                const light = document.createElement('div');
                light.className = 'light';
                light.style.background = colors[Math.floor(Math.random() * colors.length)];
                light.style.left = Math.random() * 260 + 20 + 'px';
                light.style.top = Math.random() * 300 + 50 + 'px';
                light.style.animationDelay = Math.random() * 0.8 + 's';
                tree.appendChild(light);
            }
        </script>
    </div>
</body>
</html>
